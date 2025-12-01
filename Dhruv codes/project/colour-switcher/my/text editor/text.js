let upper = document.querySelector(".button1")
let lower = document.querySelector(".button2")
let first_upper = document.querySelector(".button3")
let italic = document.querySelector(".button4")
let bold = document.querySelector(".button5")
let underline = document.querySelector(".button6")
let input = document.querySelector("#input")
let output = document.querySelector(".output")

upper.addEventListener("click", ()=>{

    let entry = input.value
    let newtext = entry.toUpperCase()

    output.innerText = newtext

})
lower.addEventListener("click", ()=>{

    let entry = input.value
    let newtext = entry.toLowerCase()

    output.innerText = newtext

})
first_upper.addEventListener("click", ()=>{

    let entry = input.value
    let newtext = entry.charAt(0).toUpperCase() + entry.slice(1)

    output.innerText = newtext

})
italic.addEventListener("click", ()=>{

    let entry = input.value

    output.style.fontStyle = "italic"

    output.innerText = entry

})

bold.addEventListener("click", () => {

    // Do NOT transform text. Just read what's already inside output.
    let entry = input.value;

    // Toggle bold without changing the text itself
    output.style.fontWeight =
        output.style.fontWeight === "bold" ? "normal" : "bold";

    output.innerText = entry; 
});

underline.addEventListener("click", ()=>{
        // output.innerText = input.value
        let entry = output.innerText
    
        output.style.textDecoration = 
            output.style.textDecoration === "underline" ? "none" : "underline"
    
        output.innerText = entry
    
    })

    input.addEventListener("click", () => {
    output.innerText = input.value;
});

    
    
    // bold.addEventListener("click", ()=>{
    
    //     let entry = input.value
    //     output.style.fontWeight = "bold"    
    
    //     output.innerText = entry
    
    // })