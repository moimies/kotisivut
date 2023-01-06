


function empty(){

    const letters = document.querySelectorAll('.letter');

        letters.forEach(letter => {
            letter.value = "";
});
    if(document.getElementById("results_id")){
        document.getElementById("results_id").remove();
    }
}



function etsi(){

    if(isAllFilled()){

        if(document.getElementById("results_id")){
             ;
        }else{
            var element = document.getElementById("content-wrapper-sanajahti");
            var results = document.createElement('div');
            //results.style.width=document.getElementById("grid-wrapper").style.width;
            //results.style.height=document.getElementById("grid-wrapper").style.height;
            results.style.width="18vw";
            results.style.height="18vw";
            //results.style.backgroundColor = "blue";
            results.style.overflow="scroll";
            results.style.padding="1vw";
            results.style.marginTop="10px";
            results.style.marginLeft="0";
            results.style.marginRight="0";
            results.style.color = 'red';
            results.style.border="5px solid black";
            results.id = "results_id";
            results.style.alignItems="left";
        
            element.appendChild(results);
        }
    
        let avaimet =[];
        $.getJSON("jsonWordsFound", function(data){
            document.getElementById("results_id").innerHTML = "";
            avaimet = Object.keys(data);
            avaimet.sort(function(a,b){
                return b.length - a.length;
            })

            for(key in avaimet){
                p = document.createElement('li');
                p.innerHTML = avaimet[key];
                p.dataset.letters = data[avaimet[key]];
                document.getElementById("results_id").appendChild(p); 

                p.addEventListener("mouseleave", function(){
                    theWordArray = this.dataset.letters.split(",");
                    theWordArray.forEach(function(letterIndex){
                        document.getElementById("letter" + letterIndex.toString()).style.backgroundColor = "white";
                    }) 

                })

                p.addEventListener("mouseover",function(){
                    //console.log(this.dataset.letters)
                    theWordArray = this.dataset.letters.split(",");
                    theWordArray.forEach(function(letterIndex){
                        document.getElementById("letter" + letterIndex.toString()).style.backgroundColor = "yellow";
                    }) 
                })
                
            }     
        })
            
   
        
       
        
        //$("#results_id").load("wordsFound");

        
    }else{
        alert("Täytä kaikki kentät")
    }
    
}

function isAllFilled(){
    isFilled = true;
    const letters = document.querySelectorAll('.letter');
    letters.forEach(letter => {
        //console.log(letter.value);
        if(letter.value === ""){
            isFilled = false;
        };
    })
    return isFilled;
}


function gridClicked(e){

    letterNum = parseInt(e.target.id.substring(6));

    if(e.key == "Backspace" && document.getElementById(e.target.id).value == "" && letterNum != 1){
        placeholder = document.getElementById("letter" + (letterNum - 1)).value;
        document.getElementById("letter" + (letterNum - 1)).value = "";
        document.getElementById("letter" + (letterNum - 1)).focus();
        document.getElementById("letter" + (letterNum - 1)).value = placeholder;
    }else if(e.key != "Backspace" && !document.getElementById(e.target.id).value == "" ){
        if(letterNum == 16 && document.getElementById(e.target.id).value != ""){
            document.getElementById("letter" + 1).focus();
        }else{
            document.getElementById("letter" + (letterNum + 1)).focus();
        }
        
    }

    


    
}

