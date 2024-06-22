import React, { useState } from 'react';
import Login from './components/Login';
import ArticleList from './components/ArticleList';
import Article from './components/Article';
import Evaluation from './components/Evaluation';

const App = () => {
    const [user, setUser] = useState(null);
    const [group, setGroup] = useState(null);
    const [selectedArticle, setSelectedArticle] = useState(null);

    const handleLogin = (username) => {
        const groupNumber = Math.ceil(parseInt(username.split('_')[1]) / 3);
        setGroup(groupNumber);
        setUser(username);
    };

    return (
        <div>
            {!user ? (
                <Login onLogin={handleLogin} />
            ) : (
                <div>
                    <ArticleList group={group} user={user} onSelectArticle={setSelectedArticle} />
                    {selectedArticle && (
                        <div>
                            <Article article={selectedArticle} />
                            <Evaluation group={group} user={user} article={selectedArticle} />
                        </div>
                    )}
                </div>
            )}
        </div>
    );
};

export default App;
