//function to change currency boxs ulternately
$(function () {
    $(".checkme").click(function (event) {
      var x = $(this).is(':checked');
      if (x == true) {
        $(this).parents(".checkbox-card").find('.passport-box').hide();
        $(this).parents(".checkbox-card").find('.apply-box').show();
      }
      else {
        $(this).parents(".checkbox-card").find('.passport-box').show();
        $(this).parents(".checkbox-card").find('.apply-box').hide();
      }
    });
  })


//function to hide and show textbox when checkbox is checked
  function showHideTextbox() {
  var box = document.getElementById("box");
  if (checkbox.checked == true) {
    box.style.display = "none";
} else {
    box.style.display = "block";
}
}

//function to hide and show textbox when checkbox is checked
function showHideTextbox() {
var chkClr = document.getElementById("chkClr");
if (checkbox.checked == true) {
    chkClr.style.display = "none";
} else {
chkClr.style.display = "block";
}
}


// Get the radio button and textbox elements
const firstradio = document.querySelector('#firstradio');
const secondradio = document.querySelector('#secondradio');

const textbox = document.querySelector('#textbox');
const textbox1 = document.querySelector('#textbox1');
// Add an event listener to the radio button
firstradio.addEventListener('click', function() {
// If the radio button is checked, enable the textbox
if (firstradio.checked) {
textbox.disabled = false;
} else {
// Otherwise, disable the textbox
textbox.disabled = true;
}
});


// Add an event listener to the radio off button
secondradio.addEventListener('click', function() {
// If the radio off button is checked, disable the textbox
if (secondradio.checked) {
textbox.disabled = true;
} else {
// Otherwise, enable the textbox
textbox.disabled = false;
}
});


// Add an event listener to the radio button
secondradio.addEventListener('click', function() {
// If the radio button is checked, enable the textbox
if (secondradio.checked) {
textbox1.disabled = false;
} else {
// Otherwise, disable the textbox
textbox1.disabled = true;
}
});
// Add an event listener to the radio off button
firstradio.addEventListener('click', function() {
// If the radio off button is checked, disable the textbox
if (firstradio.checked) {
textbox1.disabled = true;
} else {
// Otherwise, enable the textbox
textbox1.disabled = false;
}
});

// Get the radio button and textbox elements
const thirdradio = document.querySelector('#thirdradio');
const fourthradio= document.querySelector('#fourthradio');
const textbox2 = document.querySelector('#textbox2');
const textbox3 = document.querySelector('#textbox3');
// Add an event listener to the radio button
thirdradio.addEventListener('click', function() {
// If the radio button is checked, enable the textbox
if (thirdradio.checked) {
textbox2.disabled = false;
} else {
// Otherwise, disable the textbox
textbox2.disabled = true;
}
});

// Add an event listener to the radio off button
fourthradio.addEventListener('click', function() {
// If the radio off button is checked, disable the textbox
if (fourthradio.checked) {
textbox2.disabled = true;
} else {
// Otherwise, enable the textbox
textbox2.disabled = false;
}
});

// Add an event listener to the radio button
fourthradio.addEventListener('click', function() {
// If the radio button is checked, enable the textbox
if (fourthradio.checked) {
textbox3.disabled = false;
} else {
// Otherwise, disable the textbox
textbox3.disabled = true;
}
});
// Add an event listener to the radio off button
thirdradio.addEventListener('click', function() {
// If the radio off button is checked, disable the textbox
if (thirdradio.checked) {
textbox3.disabled = true;
} else {
// Otherwise, enable the textbox
textbox3.disabled = false;
}
});



//disable submit button until the all mandatory feilds are not filled
const nameInput = document.getElementById("format");
const emailInput = document.getElementById("currency_type");
const messageInput = document.getElementById("amount_entered");
const submitButton = document.getElementById("submit-btn");
function enableSubmitButton() {
if (nameInput.value && emailInput.value && messageInput.value) {
submitButton.disabled = false;
} else {
submitButton.disabled = true;
}
}
nameInput.addEventListener("input", enableSubmitButton);
emailInput.addEventListener("input", enableSubmitButton);
messageInput.addEventListener("input", enableSubmitButton);



//to make dropdown mandatory otherwisw it will give alert message
const form = document.querySelector('#sampleGenerationForm');
const dropdown = document.querySelector('#format');

form.addEventListener('submit', function(event) {
if (!dropdown.value) {
alert('Please select Format from the dropdown');
event.preventDefault();
}
});

//when format is not selected then configure button is disable
const formatinput = document.getElementById("format");
const configbutton = document.getElementById("FormatId");
function enableConfigButton() {
if ( formatinput.value) {
configbutton.disabled = false;
} else {
configbutton.disabled = true;
}
}
formatinput.addEventListener("input", enableConfigButton);