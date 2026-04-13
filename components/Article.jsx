import React from 'react'

function Article(props) {
    const [count, setCount] = React.useState(0)

    const handleIncrement = () => {
        setCount(count + 1)
    }

    return (
        <div>
            <h1>Article</h1>
            <h3>{props.title}</h3>
            <p>lorem ipsum dolor sit amet, consectetur adipiscing elit  </p>
            <h2>{count}</h2>
            <button onClick={handleIncrement}>Like ({count})</button>
        </div>
    )
}

export default Article



import styled from 'styled-components';
const Button = styled.button`
    background-color: #4CAF50; 
    border: none;
    color: white;
`;

<Button>Click Me</Button>

