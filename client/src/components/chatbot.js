// Imports chatbot & theme component libraries
import ChatBot from 'react-simple-chatbot';
import { ThemeProvider } from 'styled-components';

// Preset options for students to select
// Contains basic syllabus information
import { Steps } from '../assets/Steps';

// Contains the theme and styling of the chatbot
import { theme } from '../assets/theme';

// Syllabus chatbot avatar
import temocLogo from '../assets/temoc.png';



function ChatbotComponent() {
    return (
        <div className="App">
            <ThemeProvider theme={theme}>
                <ChatBot
                    headerTitle="Advanced Algorithms Syllabus Chatbot"
                    recognitionEnable={true}
                    contentStyle={{ height: '85vh' }}
                    style={{ height: '100%', width: '100%' }}
                    steps={Steps}
                    botAvatar={temocLogo}
                    hideUserAvatar={true}
                    botDelay = {600}
                    userDelay = {600}
                />
            </ThemeProvider>
        </div>
    );
}

// Exports to be referenced by app.js file
export default ChatbotComponent;