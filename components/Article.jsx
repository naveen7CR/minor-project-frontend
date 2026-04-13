import React from 'react'



function Article(props) {
    const [count, setCount] = React.useState(0)

    const handleIncrement = () => {
        setCount(count + 1)
    }
    const handleDecrement = () => {
        setCount(count - 1)
    }

    return (
        <div>
            <h1>Article</h1>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptas, voluptate.</p>
            <h3>{props.title}</h3>
            <h3>{count}</h3>
            <button onClick={handleIncrement}>Increase</button>
            <button onClick={handleDecrement}>Decrease</button>
        </div>
    )
}


export default Article




// import React, { Component } from 'react'

// class Article extends Component {
//     constructor(props) {
//         super(props)
//         this.state={
//             count:0
//         }
//     }
//     handleIncrement=()=>{
//         this.setState({count:this.state.count+1})
//     }
//     handleDecrement=()=>{
//         this.setState({count:this.state.count-1})
//     }

//   render() {
//     return (
//       <div>
//         <h1>Article</h1>
//         <h3>{this.props.title}</h3>
//         <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptas, voluptate.</p>
//         <button onClick={this.handleIncrement}>Increase</button><br></br>
//         <button onClick={this.handleDecrement}>Decrease</button>
//         <h3>Count: {this.state.count}</h3>
//     </div>
//     )
//   }
// }

// export default Article



import styled from 'styled-components';
const Button = styled.button`
    background-color: #4CAF50; 
    border: none;
    color: white;
`;

<Button>Click Me</Button>

