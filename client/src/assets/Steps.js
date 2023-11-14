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
        message: "Give a short response: " + query.value,
      },
    })
      .then((response) => {
        this.setState({ answer: response.data.data});
        console.log("response produced");
        this.props.triggerNextStep({trigger: '10'});
      })
      .catch((error) => {
        console.error('API error:', error);
        this.setState({ error: "An error occurred." });
        this.props.triggerNextStep({trigger: '10'});
      });
  }

    render() {
        const { answer, error} = this.state;

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
    }, 
    {
        id: '4',
        user: true,
        trigger: '5'
    },
    {
        id: '5',
        message: "Placeholder Syllabus respone",
        trigger: '10'
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
        waitAction: true
    },
    {
        id:'10',
        message: "What else would you like help with?",
        trigger:'2'
    }
];




