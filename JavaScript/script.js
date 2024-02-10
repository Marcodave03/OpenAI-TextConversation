const { Configuration, OpenAIApi } = require("openai");
const readline = require("readline");

// Setup readline interface
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Your OpenAI API Key
const apiKey = "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"; 

// Configure OpenAI API
const configuration = new Configuration({
  apiKey: apiKey,
});
const openai = new OpenAIApi(configuration);

// Function to chat with OpenAI
const chatWithOpenAI = (prompt) => {
  openai.createCompletion({
    model: "text-davinci-003", // You can update the model name based on your requirements
    prompt: prompt,
    temperature: 0.7,
    max_tokens: 150,
    n: 1,
    stop: null,
  }).then(response => {
    console.log(`OpenAI: ${response.data.choices[0].text.trim()}`);
    askQuestion(); // Ask the next question after displaying the response
  }).catch(error => console.error("Error calling OpenAI:", error));
};

// Function to ask questions
const askQuestion = () => {
  rl.question("You: ", (input) => {
    if(input.toLowerCase() === "exit") { // Type "exit" to quit
      rl.close();
    } else {
      chatWithOpenAI(input);
    }
  });
};

console.log("OpenAI Chat Terminal. Type 'exit' to quit.");
askQuestion();
