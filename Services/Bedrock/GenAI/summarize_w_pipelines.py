from transformers import pipeline

summarizer = pipeline("summarization", "facebook/bart-large-cnn")

article = "In a building on the edge of a business park outside Sheffield, researcher Ihab Ahmed is preparing to fire up a small jet engine. Originally used as an auxiliary power unit for a commercial airliner, it has been turned into a testbed for new fuels developed in a laboratory next door. The arrangement is a centrepiece of Sheffield University’s Sustainable Fuels Innovation Centre (SAF-IC), a research facility set up to allow synthetic fuels to be prepared and evaluated on a small scale, before being put into large scale production. On a bank of computer screens in a nearby control room, Ihab can monitor the engine as it starts with a burst of flame and powers up. Sensors tell him what the engine is doing in real time – and allow the exhaust gases to be continually analysed. Sustainable fuels are synthetic alternatives to fossil fuels, made from renewable sources. These can include waste cooking oils, vegetable fats and agricultural waste, as well as captured carbon dioxide."

print(summarizer(article, max_length=150, min_length=50, do_sample=False))