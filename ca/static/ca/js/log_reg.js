

function myf(){
  var flag=1;
  if (document.getElementById('fname').value==="")
  {
    document.getElementById('fname').classList.add('is-invalid');
    document.getElementById('fname').focus();
    flag=0;
    
  }
  else{
    document.getElementById('fname').classList.remove('is-invalid');
  }


  if (!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(document.getElementById('email').value)))
  {
    document.getElementById('email').classList.add('is-invalid');
    document.getElementById('email').focus();
    flag=0;
    
  }
  else {
    document.getElementById('email').classList.remove('is-invalid');
  }


  if (parseInt(document.getElementById('phone').value,10)<1000000000&&parseInt(document.getElementById('phone').value,10)>9999999999||document.getElementById('phone').value==="") {
    document.getElementById('phone').classList.add('is-invalid');
    document.getElementById('phone').focus();
    flag=0;

    
  }
  else {
    document.getElementById('phone').classList.remove('is-invalid');
  }


  if (document.getElementById('sel1').value==="")
  {
    document.getElementById('sel1').classList.add('is-invalid');
    document.getElementById('sel1').focus();
    flag=0;
    
  }
  else{
    document.getElementById('sel1').classList.remove('is-invalid');
  }


  if (document.getElementById('college').value==="")
  {
    document.getElementById('college').classList.add('is-invalid');
    document.getElementById('college').focus();
    flag=0;
  }
  else{
    document.getElementById('college').classList.remove('is-invalid');
  }


  if (document.getElementById('sel2').value==="")
  {
    document.getElementById('sel2').classList.add('is-invalid');
    document.getElementById('sel2').focus();
    flag=0;
  }
  else{
    document.getElementById('sel2').classList.remove('is-invalid');
  }


  if (document.getElementById('comment').value==="")
  {
    document.getElementById('comment').classList.add('is-invalid');
    document.getElementById('comment').focus();
    flag=0;
    
  }
  else{
    document.getElementById('comment').classList.remove('is-invalid');
  }
/*
  if (document.getElementById('my-file-selector').files.length===0 || document.getElementById('my-file-selector').files.length > "5000")
  {
    alert('Please upload your JPEG/PNG image of max size 5MB')
    flag=0;
    
  }
  */


  
  if (flag==1) {
    return true;

  }

  else {
    
    
    return false;
  }

}