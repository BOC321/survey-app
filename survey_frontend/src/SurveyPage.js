import React, { useState } from 'react';

function SurveyPage({ questions, onAnswer }) {
    const [currentQuestion, setCurrentQuestion] = useState(0);

    const handleAnswer = (answer) => {
        onAnswer(questions[currentQuestion].id, answer);
        setCurrentQuestion(currentQuestion + 1);
    };

    return (
        <div>
            <h1>{questions[currentQuestion].text}</h1>
            {questions[currentQuestion].answers.map((answer) => (
                <button key={answer.id} onClick={() => handleAnswer(answer)}>
                    {answer.text}
                </button>
            ))}
        </div>
    );
}

export default SurveyPage;
