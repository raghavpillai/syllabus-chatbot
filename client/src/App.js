import ChatBot from 'react-simple-chatbot';
 
const steps = [
  {
      id: '0',
      message: 'Hello!',

      // This calls the next id
      // i.e. id 1 in this case
      trigger: '1',
  }, {
      id: '1',

      // This message appears in
      // the bot chat bubble
      message: 'What would you like help with?',
      trigger: '2'
  }, {
      id: '2',

      // Here we want the user
      // to enter input
      user: true,
      trigger: '3'
  }, {
    id: '3',
    message: "Sure, I will help you with the following: {previousValue}",
    trigger: '1'
  }
];
 
function App() {
    return (
        <div className="App">
            <h1>Syllabus Chatbot</h1>
            <ChatBot
              style= {{height: '100vh', width: '100%'}}
              steps={steps}
            />
        </div>
    );
}
 
export default App;
