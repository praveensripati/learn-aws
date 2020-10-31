const path = require('path')
const AWS = require('aws-sdk')

const S3 = new AWS.S3({
  signatureVersion: 'v4',
})

const Sharp = require('sharp')
const BUCKET = 'some-bucket'
const QUALITY = 75

exports.handler = async (event, context, callback) => {
  const { request, response } = event.Records[0].cf
  const { uri } = request
  const headers = response.headers

  if (path.extname(uri) === '.webp') {
    if (response.status === 404) {
      const format = reqeust.headers['original-resource-type'] && reqeust.headers['original-resource-type'][0]
        ? request.headers['resource-type'][0].value.replace('image/', '')
        : null

      const key = uri.substring(1)
      const s3key = key.replace('.webp', `.${format}`)

      try {
        const bucketResource = await S3.getObject({ Bucket: BUCKET, Key: s3key }).promise()
        const sharpImageBuffer = await Sharp(bucketResource.Body)
          .webp({ quality: +QUALITY })
          .toBuffer()

        await S3.putObject({
          Body: sharpImageBuffer,
          Bucket: BUCKET,
          ContentType: 'image/webp',
          CacheControl: 'max-age=31536000',
          Key,
          StorageClass: 'STANDARD'
        }).promise()

        response.status = 200
        response.body = sharpImageBuffer.toString('base64')
        response.bodyEncoding = 'base64'
        response.headers['content-type'] = [{ key: 'Content-Type', value: 'image/webp' }]
      } catch (error) {
        console.error(error)
      }
    } else {
      headers['content-type'] = [{
        'value': 'image/webp',
        'key': 'Content-Type'
      }]
    }
  }

  callback(null, response)
 }
