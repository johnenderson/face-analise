import boto3

s3 = boto3.resource('s3')
client = boto3.client('rekognition')


def lista_imagens():
    imagens = []
    bucket = s3.Bucket('fa-img-jes-alura')
    for imagem in bucket.objects.all():
        imagens.append(imagem.key)
    return imagens


def indexa_colecao(imagens):
    for i in imagens:
        response = client.index_faces(
            CollectionId='faces',
            # DetectionAttibutes=[''],
            ExternalImageId=i[:-4],
            Image={
                'S3Object': {
                    'Bucket': 'fa-img-jes-alura',
                    'Name': i,
                },
            },
        )


imagens = lista_imagens()
indexa_colecao(imagens)
