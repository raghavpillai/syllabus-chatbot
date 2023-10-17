// Imports chatbot component's library
import ChatBot from 'react-simple-chatbot';

// Preset options for students to select
// Contains basic syllabus information
import { steps } from '../assets/steps';

function ChatbotComponent() {
    return (
        <div className="App">
            <ChatBot
                headerTitle="Advanced Algorithms Syllabus Chatbot"
                contentStyle={{ height: '85vh' }}
                style={{ height: '100%', width: '100%' }}
                steps={steps}
            />
        </div>
    );
}

// Exports to be referenced by app.js file
export default ChatbotComponent;