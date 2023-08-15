function hide_cans(){
	var cans = document.getElementsByClassName('cans');
	for (var i = 0; i < cans.length; i++){
		cans[i].style.transform = 'rotateY(90deg)';
	}
}

function hide_fields(){
	var id_aux = '';
	var fields = document.getElementsByClassName('name-fields');
	var words = document.getElementsByClassName('fl_name');
	for (var i = 0; i < fields.length; i++){
		if (fields[i].value != ''){
			id_aux = fields[i].id;
			id_aux = id_aux.replace('new_name', 'edit');
			document.getElementById(id_aux).click();
		}
		fields[i].style.position = 'absolute';
		fields[i].style.visibility = 'hidden';
		words[i].style.display = 'block';
	}
}

function show_cans(id){
	var can = document.getElementById('delete' + id);
	if (can.style.transform == 'rotateY(90deg)'){
		hide_cans();
		can.style.transform = 'rotateY(0deg)';
	}else{
		hide_cans();
	}
}

function show_fields(id){
	hide_fields();
	var name_aux = document.getElementById(id);
	name_aux.style.display = 'none';
	var str_aux = id.replace('folderName', '');
	str_aux = 'new_name' + str_aux;
	document.getElementById(str_aux).style.position = 'static';
	document.getElementById(str_aux).style.visibility = 'visible';
}

function file_name(){
	document.getElementById('upload-file-form').style.width = '350px';
	document.getElementById('upload-file-form').style.transform = 'scaleX(1.1)';
	document.getElementById('upload-file-form').style.transform = 'translateX(-15px)';
	document.getElementById('upload-file-form').style.transitionDuration = '0.5s';
	var name = document.getElementById('uploaded-file').value;
	document.getElementById('uploaded-file-name').innerHTML = name;
	document.getElementById('upload-btn').removeAttribute('disabled');
}

document.addEventListener('DOMContentLoaded', function(){
	var links = document.getElementsByClassName('folder-pic');
	var nms = document.getElementsByClassName('fl_name');
	var url = window.location.href;
	for (var i = 0; i < links.length; i++){
		links[i].href = url + '-' + nms[i].innerHTML;
	}
	var dots_aux = document.getElementsByClassName('dots');
	if (dots_aux.length != 0){
		dots_aux[0].click();
	}
	var btns_aux = document.getElementsByClassName('left-btns');
	var cont_aux = document.getElementsByClassName('btn-container');
	for (var i = 0; i < btns_aux.length; i++){
		if (btns_aux[i].innerHTML == "Files"){
			btns_aux[i].style.backgroundColor = "#f47a60";
			btns_aux[i].style.transform = "translate(10px)";
			cont_aux[i].classList.remove('btn-container');
		}
	}
});