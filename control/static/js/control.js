/**
 * Created by ryan on 3/25/18.
 */

function initializeControls(controls_url){
    // Keyboard Controls
    $.get(controls_url, function(data){
        var keyboard_controls = data.keyboard;
        var forward = keyboard_controls.FORWARD;
        var right = keyboard_controls.RIGHT;
        var left = keyboard_controls.LEFT;
        var back = keyboard_controls.BACK;
        $(window).on('keydown', function(event){
            if(event.keyCode == forward){
                sendMovementRequest('FORWARD');
            }else if(event.keyCode == right){
                sendMovementRequest('RIGHT');
            }else if(event.keyCode == left){
                sendMovementRequest('LEFT');
            }else if(event.keyCode == back){
                sendMovementRequest('BACK');
            }
        });
    });
}

function sendMovementRequest(action){
    csrf_token = $('input[name=csrfmiddlewaretoken]').val();
    $.post('/control/movement', {'action': action, 'csrfmiddlewaretoken': csrf_token}, function(data){
        alert('Sent Key Press ' + data.action);
    });
}