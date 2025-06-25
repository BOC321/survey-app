import React, { useEffect, useState } from 'react';
import axios from 'axios';
import SurveyPage from './components/SurveyPage';

function App() {
    const [questions, setQuestions] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/api/questions/')
            .then(response => setQuestions(response.data))
            .catch(error => console.error(error));
    }, []);

    const handleAnswer = (questionId, answer) => {
        axios.post('http://localhost:8000/api/responses/', {
            question: questionId,
            answer: answer.id
        }).catch(error => console.error(error));
    };

    return (
        <div>
            {questions.length > 0 ? (
                <SurveyPage questions={questions} onAnswer={handleAnswer} />
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
}

export default App;
