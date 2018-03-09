window.onload = function(){

    var num = 0;     //控制头像改变
    var iNow = -1;    //用来累加改变左右浮动
    var btn = document.getElementById('btn');
    var text = document.getElementById('text');

    var content = document.getElementsByTagName('ul')[0];
    //img is content's icno,span is content's text.
    var img = content.getElementsByTagName('img');
    var span = content.getElementsByTagName('span');

    btn.onclick = function(){
        if(text.value === '' || null){
            alert('不能发送空消息');
        }else {
            console.log("Enter in content function");

            content.innerHTML += '<li><img src="img/logo.jpg"><span>'+text.value+'</span></li>';
            iNow++;

            //num changes depend on user or server is talking.
            //adjust their location by css className.
            if(num === 0){
                img[iNow].className += 'imgright';
                span[iNow].className += 'spanright';
            }else {
                img[iNow].className += 'imgleft';
                span[iNow].className += 'spanleft';
            }
            text.value = '';
            // 内容过多时,将滚动条放置到最底端
            content.scrollTop=content.scrollHeight;
        }
    }
};