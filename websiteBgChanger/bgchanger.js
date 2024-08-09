const buttons = document.querySelectorAll('.button')
const body = document.querySelector("body")

buttons.forEach(function(button){
    button.addEventListener('click', function(e){ //e is event
        if(e.target.id === 'grey'){
            body.style.backgroundColor = e.target.id
        }
        else if(e.target.id === 'white'){
            body.style.backgroundColor = e.target.id
            body.style.color = 'black'
        }
        else if(e.target.id === 'blue'){
            body.style.backgroundColor = e.target.id
        }
        else if(e.target.id === 'yellow'){
            body.style.backgroundColor = e.target.id
        }
        else if(e.target.id === 'green'){
            body.style.backgroundColor = e.target.id
        }
        else if(e.target.id === 'red'){
            body.style.backgroundColor = e.target.id
        }
        else if(e.target.id === 'black'){
            body.style.backgroundColor = e.target.id
            body.style.color = 'white'
        }
    })
})