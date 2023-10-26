import React, { Component } from 'react';
import PropTypes from 'prop-types';
import axios from "axios";

class Question extends Component {
  constructor(props) {
    super(props);

    this.state = {
      answer: null,
      error: null,
    };
  }

  componentDidMount() {
    const { steps } = this.props;
    const { query } = steps;
    console.log('Starting API call');
    this.setState({ query: query.value });
    axios({
      method: "GET",
      url: "http://127.0.0.1:8000/openai/v1/get_response",
      params: {
        message: query.value,
      },
    })
      .then((response) => {
        this.setState({ answer: response.data.data});
        console.log("response produced")
      })
      .catch((error) => {
        console.error('API error:', error);
        this.setState({ error: "An error occurred." });
      });
  }

    render() {
        const { answer, error, query } = this.state;

        return (
            <div>
                {error ? (
                    <div>Error: {error}</div>
                ) : (
                    <div>{answer}</div>
                )}
            </div>
        );
    }
}

Question.propTypes = {
    steps: PropTypes.object,
    };
    
    Question.defaultProps = {
    steps: undefined,
    };

export const Steps = [
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
        trigger: 'query'
    },
    {
        id: 'query',
        user: true,
        trigger: 'answer'
    },
    {
        id: 'answer',
        component:  <Question />,
        asMessage: true,
        trigger:'10'
    },
    {
        id:'10',
        delay:5000,
        message: "What else would you like help with?",
        trigger:'2'
    }
];




