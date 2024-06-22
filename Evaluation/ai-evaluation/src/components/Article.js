import React from 'react';

const Article = ({ article }) => {
    return (
        <div>
            <h2>{article.title}</h2>
            <pre>{article.content}</pre>
        </div>
    );
};

export default Article;
