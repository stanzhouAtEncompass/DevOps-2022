import boto3


def translator(text, source='en', target='zh'):
    """This uses AWS Translate to the Translate Text
    Valid Values: de | en | es | fr | it | ja | ko | pt | zh | zh-TW
    """

    print(f"Passwd in source language: {source}") 
    print(f"Passwd in target language: {target}") 
    client = boto3.client('translate')

    response = client.translate_text(
       Text=text,
       SourceLanguageCode=source,
       TargetLanguageCode=target,
    )
    return response['TranslatedText']
