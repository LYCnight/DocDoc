import React, { useState } from 'react';
import axios from 'axios';

const Evaluation = ({ group, user, article }) => {
    const [evaluation, setEvaluation] = useState({
        Fluency: 3,
        Coherence: 3,
        Consistency: 3,
        Relevance: 3,
        Length: 3,
        Structure: 3,
        Text_style: 3,
        Adversarial_success: 3,
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setEvaluation({ ...evaluation, [name]: parseInt(value) });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post(`/evaluate/${group}/${user}/${article.shuffled_id}`, evaluation);
            alert('Evaluation submitted!');
        } catch (err) {
            console.error('Error submitting evaluation', err);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            {Object.keys(evaluation).map((key) => (
                <div key={key}>
                    <label>{key}</label>
                    <input
                        type="number"
                        name={key}
                        value={evaluation[key]}
                        onChange={handleChange}
                        min="1"
                        max="5"
                    />
                </div>
            ))}
            <button type="submit">Submit</button>
        </form>
    );
};

export default Evaluation;
