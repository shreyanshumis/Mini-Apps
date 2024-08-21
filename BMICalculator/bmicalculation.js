const form = document.querySelector('form')

//stopping get/post method
form.addEventListener('submit', function(subEvent){
    subEvent.preventDefault()

    const height = parseFloat(document.querySelector('#height').value); //you get form values using this and then convert it's type
    const weight = parseFloat(document.querySelector('#weight').value);
    const results = document.querySelector('#results');
    const statement = document.querySelector('#statement');

    if(height === '' || height < 0 || isNaN(height)){
        results.innerHTML = `Please give a valid height ${height}`
    } else if(weight === '' || height < 0 || isNaN(weight)){
        results.innerHTML = `Please give a valid height ${weight}`
    } else {
        const bmi = (weight/((height*height)/10000)).toFixed(2)
        //the result
        results.innerHTML = `<span>${bmi}</span>`
        if(bmi < 18.60){
            statement.innerHTML = `<span>you are Underweight</span>`;
        }
        else if (bmi >= 18.60 && bmi < 24.90){
            statement.innerHTML = `<span>you are at a normal weight</span>`;
        }
        else {
            statement.innerHTML = `<span>you're Overweight</span>`;
        }
    }
})