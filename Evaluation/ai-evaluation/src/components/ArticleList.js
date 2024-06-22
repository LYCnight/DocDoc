import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ArticleList = ({ group, user, onSelectArticle }) => {
    const [articles, setArticles] = useState([]);

    useEffect(() => {
        const fetchArticles = async () => {
            try {
                const response = await axios.get(`/articles/${group}/${user}`);
                setArticles(response.data);
            } catch (err) {
                console.error('Error fetching articles', err);
            }
        };

        fetchArticles();
    }, [group, user]);

    return (
        <div>
            <h2>Articles</h2>
            <ul>
                {articles.map((article) => (
                    <li key={article.shuffled_id} onClick={() => onSelectArticle(article)}>
                        {article.title}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ArticleList;
