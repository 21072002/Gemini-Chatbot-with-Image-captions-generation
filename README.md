# Gemini-Chatbot-with-Image-captions-generation
### Replacing `config.json` with Your Gemini API Key

To configure the Gemini Chatbot for image caption generation, you need to replace the existing `config.json` file with your own API key.

1. **Locate the `config.json` file:**
   - The `config.json` file is located in the root directory of this repository. This file contains configuration settings, including the API key needed to access Gemini services.

2. **Obtain your Gemini API Key:**
   - If you don't already have a Gemini API key, you'll need to create an account on the [Gemini website](https://gemini.com). Once logged in, navigate to the API section to generate your API key.

3. **Update the `config.json` file:**
   - Open the `config.json` file in any text editor.
   - Replace the placeholder `"YOUR_GEMINI_API_KEY"` with your actual Gemini API key. 
   
   Example:
   ```json
   {
       "gemini_api_key": "your_actual_gemini_api_key_here"
   }
   ```

4. **Save and close the file:**
   - After updating the API key, save the `config.json` file and close the text editor.

5. **Run the chatbot:**
   - You can now run the chatbot with your configured API key. The chatbot should be able to generate image captions using the Gemini API.

