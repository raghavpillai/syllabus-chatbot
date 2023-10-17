// Imports chatbot & theme component libraries
import ChatBot from 'react-simple-chatbot';
import { ThemeProvider } from 'styled-components';

// Preset options for students to select
// Contains basic syllabus information
import { steps } from '../assets/steps';

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
                    contentStyle={{ height: '85vh' }}
                    style={{ height: '100%', width: '100%' }}
                    steps={steps}
                    botAvatar={temocLogo}
                    hideUserAvatar={true}
                />
            </ThemeProvider>
        </div>
    );
}

// Exports to be referenced by app.js file
export default ChatbotComponent;