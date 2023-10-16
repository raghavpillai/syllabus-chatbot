import ChatBot from 'react-simple-chatbot';

const steps = [
  {
    id: '0',
    message: 'Hello!',

    // This calls the next id
    // i.e. id 1 in this case
    trigger: '1',
  },
  {
    id: '1',
    message: 'What would you like help with?',

    // This calls the next id
    // i.e. id 1 in this case
    trigger: '2',
  }, {
    id: '2',
    options: [
      { value: "advanced algroithm concepts", label: 'Concepts', trigger: '9' },
      { value: "questions about the syllabus", label: 'Syllabus Question', trigger: '3' },
    ],
  },
  {
    id: '3',
    message: "Sure, which syllabus topic do you need help with?",
    trigger: '4'
  }, {

    id: '4',
    options: [
      { value: "Meeting Times", label: 'Meeting Times', trigger: '5' },
      { value: "Exam Dates", label: 'Exam Dates', trigger: '6' },
      { value: "Professor Information", label: 'Professor Information', trigger: '7' },
      { value: "Other", label: 'Other', trigger: '8' },
    ],
  },
  {
    id: '5',
    message: "This class meets on Tuesdays & Thursdays 10:00 am – 11:15 am",
    trigger: '1'
  },
  {
    id: '6',
    message: "Exam 1: October 3, Exam 2: November 7, Exam 3: December 12",
    trigger: '1'
  },
  {
    id: '7',
    message: "Name: Anjum Chida \n" +
      "Phone: 972-883-2185\n" +
      "Email: anjum.chida@utdallas.edu\n" +
      "Office: ECSS 4.230\n" +
      "Office Hours: In-person 10:00 am to 12:00 noon\n" +
      "(Mondays & Wednesdays)\n" +
      "(Or by appointment, additional meetings can be virtual via MS-Teams)",
    trigger: '1'
  },
  {
    id: '8',
    message: "PlaceHolder",
    trigger: '1'
  },
  {
    id: '9',
    message: "What question do you have about advanced algorithms?",
    trigger: '10'
  },
  {
    id: '10',
    user: true,
    trigger: '11'
  },
  {
    id: '11',
    message: "Sure, I will help you with the following: {previousValue}",
    trigger: '1'
  }
];

function App() {
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

export default App;
