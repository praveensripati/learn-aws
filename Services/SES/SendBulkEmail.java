import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.services.simpleemail.AmazonSimpleEmailServiceClient;
import com.amazonaws.services.simpleemail.model.Body;
import com.amazonaws.services.simpleemail.model.Content;
import com.amazonaws.services.simpleemail.model.Destination;
import com.amazonaws.services.simpleemail.model.Message;
import com.amazonaws.services.simpleemail.model.SendEmailRequest;

public class SendBulkEmail {
	public static void main(String[] args) throws Exception {

		int numOfMailsPerSec = 5;
		int sleepTime = 0;

		SendEmailRequest request = new SendEmailRequest()
				.withSource("something@gmail.com");
		List<String> toAddresses = new ArrayList<String>();

		// Open the file that is the first
		// command line parameter
		FileInputStream fstream = new FileInputStream(
				"/home/praveensripati/Workspace/AWS/SendEMail/src/testfile.txt");
		// Get the object of DataInputStream
		DataInputStream in = new DataInputStream(fstream);
		BufferedReader br = new BufferedReader(new InputStreamReader(in));
		String strLine;
		// Read File Line By Line
		while ((strLine = br.readLine()) != null) {
			// Print the content on the console
			// System.out.println(strLine);
			toAddresses.add(strLine);
		}
		// Close the input stream
		in.close();

		Content subjContent = new Content()
				.withData("Building Exciting Careers with Big Data using Hadoop");
		Message msg = new Message().withSubject(subjContent);
		// Include a body in both text and HTML formats
		// Content textContent = new Content()
		// .withData("Hello - I hope you're having a good day - plain text.");
		Content htmlContent = new Content()
				.withData("<html><head></head><body></body></html>");
		Body body = new Body().withHtml(htmlContent);
		msg.setBody(body);
		request.setMessage(msg);
		// Set AWS access credentials
		AmazonSimpleEmailServiceClient client = new AmazonSimpleEmailServiceClient(
				new BasicAWSCredentials("Key1",
						"Key2"));

//		List<String> selfAddresses = new ArrayList<String>();
//		selfAddresses.add("something@gmail.com");

		List<String> toNAddresses = new ArrayList<String>();

		for (int i = 0; i < toAddresses.size(); i++) {

			System.out.println("# = " + i);

			if ((i % numOfMailsPerSec == 0) && (i != 0)) {

				Destination dest = new Destination();
//						.withToAddresses(selfAddresses);

				dest.withBccAddresses(toNAddresses);

				// commented the below for testing
				request.setDestination(dest);

				try {
					client.sendEmail(request);
					System.out.println("Sent " + numOfMailsPerSec
							+ " emails !!!!");
				} catch (Exception e) {
					e.printStackTrace();
				}
				// System.out.println("\n\nSending mail done !!!");

				// sleep for a second before sending the next set of mails
				Thread.sleep(sleepTime);
				// System.out.println("Creating a new object for toNAddresses");
				toNAddresses = new ArrayList<String>();
			}

			toNAddresses.add(toAddresses.get(i));
//			System.out.println("Writing " + toAddresses.get(i)
//					+ " to the toNAddresses variable");

		}

		// sleep for a second before sending the next set of mails
		Thread.sleep(sleepTime);
		Destination dest = new Destination();//.withToAddresses(selfAddresses);

		dest.withBccAddresses(toNAddresses);

		// commented the below for testing
		request.setDestination(dest);

		try {
			client.sendEmail(request);
			System.out.println("Sent " + numOfMailsPerSec + " emails !!!!");
		} catch (Exception e) {
			e.printStackTrace();
		}
		System.out.println("\n\nSending mail done - Final!!!");
	}

}
