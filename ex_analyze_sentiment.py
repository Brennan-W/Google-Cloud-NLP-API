def sample_analyze_sentiment(text_content, language_v1, enums):
    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'I am so happy and joyful.'

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/l anguages
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_sentiment(document, encoding_type=encoding_type)
    # Get overall sentiment of the input document
    print(u"Document sentiment score: {}".format(response.document_sentiment.score))
    print(
        u"Document sentiment magnitude: {}".format(
            response.document_sentiment.magnitude
        )
    )
    print('***')

    # Get sentiment for all sentences in the document
    for sentence in response.sentences:
        magnitude = sentence.sentiment.magnitude
        sentiment = sentence.sentiment.score
        if ((magnitude > 0.50) | (abs(sentiment) > 0.75)):
            print(u"Sentence text: {}".format(sentence.text.content))
            print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
            print(u"Sentence sentiment magnitude: {}\n".format(sentence.sentiment.magnitude))

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(u"\nLanguage of the text: {}".format(response.language))
