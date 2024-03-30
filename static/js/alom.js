
        
function searchContent() {
                   
    var elements = document.querySelectorAll(".check_counter_container");
            
            
    elements.forEach(function(element) {
        var content = element.textContent.toLowerCase();
        if (content.includes(query)) {
                    
            element.style.display = "block";
               
            element.scrollIntoView({ behavior: 'auto', block: 'start' });
        } else {
          
            element.style.display = "none";
        }
    });
}
        
        
document.getElementById("searchInput").addEventListener("change", function(event){
    console.log('Input value changed:', Number(event.target.value));
    var targetElement = document.getElementById(`each-${Number(event.target.value)*2-8}`)
    targetElement.scrollIntoView({
behavior: 'auto' 
});});
