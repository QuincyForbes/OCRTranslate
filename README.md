# OCRTranslate

OCRTranslate is a powerful tool that leverages the capabilities of Google's AI Vision API and OpenAI's API to recognize text and provide translations in various languages using prompts.

## Requirements

Before using OCRTranslate, make sure you have the following requirements in place:

1. **Google Service Account Credential File**: You need to add the Google Service Account credential file `cred.json` to the main folder of the project. This file is necessary to authenticate and access the Google AI Vision API.

2. **OpenAI API Key**: Add your OpenAI API key to the `config.yaml` file. This key allows OCRTranslate to interact with the OpenAI API and utilize its translation capabilities.

## Getting Started

To get started with OCRTranslate, follow these steps:

1. Ensure you have met all the requirements mentioned above.
2. Clone or download the OCRTranslate repository to your local machine.
3. Add the Google Service Account credential file to the main folder. If you don't have one, refer to the Google Cloud documentation to create a service account and obtain the necessary credentials.
4. Open the `config.yaml` file and insert your OpenAI API key. If you don't have an API key, sign up for an account on the OpenAI website and generate a new key.
5. Install the required dependencies by running the following command:
    <pre>pip install -r requirements.txt</pre>
6. Once the dependencies are installed, you are ready to use OCRTranslate.

## Usage

To use OCRTranslate, follow these steps:

1. Run the main script by executing the following command:
 <pre>
python main.py
</pre>
2. OCRTranslate will to start a flask server running on http://127.0.0.1:5000 which you can provide an image containing the text you want to recognize and translate.
3. After processing the image, OCRTranslate will display the recognized text, and the translation(This can take sometime based on the complexity the request). 

## Contributions

Contributions to OCRTranslate are welcome! If you encounter any issues, have suggestions, or want to add new features, please submit a pull request on the GitHub repository.
## Examples
![test 2](https://github.com/QuincyForbes/OCRTranslate/assets/74159902/97dd782a-2637-4cae-9132-41d90e4d7a01)

## License

OCRTranslate is licensed under the [MIT License](LICENSE).

## Disclaimer

OCRTranslate is an open-source project and utilizes third-party APIs for its functionality. Please ensure that you comply with the terms of service and usage limits of the Google AI Vision API and OpenAI API when using OCRTranslate. The project developers are not responsible for any misuse or violation of API terms.

For more information, refer to the [Google Cloud Platform](https://cloud.google.com/docs/) and [OpenAI](https://platform.openai.com/docs/) documentation.

---

By following these instructions, you can effectively set up OCRTranslate and leverage its powerful capabilities for text recognition and translation.
