import React, { Component } from "react";
import PropTypes from "prop-types";
import Latex from "react-latex";
import 'katex/dist/katex.min.css';

class Question extends Component {
  constructor(props) {
    super(props);

    this.state = {
      answer: "",
      error: null,
    };

    // Bind the processText method to 'this'
    this.processText = this.processText.bind(this);
  }

  processText({ done, value }) {
    if (done) {
      console.log("Stream complete");
      this.props.triggerNextStep({ trigger: "1" });
      return;
    }

    const result = this.decoder.decode(value);
    try {
      const data = JSON.parse(result);

      if (data.type === "partial") {
        this.setState({ answer: data.content });
      } else if (data.type === "full") {
        this.setState({ answer: data.content });
      }
    } catch (error) {
      console.error("Error parsing JSON:", error);
    }

    return this.reader.read().then(this.processText);
  }

  componentDidMount() {
    const { steps } = this.props;
    const { query } = steps;
    console.log("Starting API call");
    this.setState({ query: query.value });
    fetch("http://127.0.0.1:8080/api/response/stream", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        message: "Give a short response: " + query.value,
      }),
    })
      .then((response) => {
        this.reader = response.body.getReader();
        this.decoder = new TextDecoder("utf-8");

        return this.reader.read().then(this.processText);
      })
      .catch((error) => {
        console.error("API error:", error);
        this.setState({ error: "An error occurred." });
        this.props.triggerNextStep({ trigger: "1" });
      });
  }

  render() {
    const { answer, error } = this.state;

    return (
      <div>
        {error ? (
          <div>Error: {error}</div>
        ) : (
          <div>
            <Latex>{answer}</Latex>
          </div>
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
    id: "0",
    message:
      "Hello! This chatbot answers questions regarding advanced algorithm concepts as well as syllabus questions about CS4349.",

    // This calls the next id
    // i.e. id 1 in this case
    trigger: "1",
  },
  {
    id: "1",
    message: "What is your question?",
    trigger: "query",
  },
  {
    id: "query",
    user: true,
    trigger: "answer",
  },
  {
    id: "answer",
    component: <Question />,
    asMessage: true,
    waitAction: true,
  },
];
