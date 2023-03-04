function run() {
    var cmd = "g++ -Wall main.cpp -o main_prog && echo 'Compilation: SUCCESS."
        + " Program output is:\n' && ./main_prog && echo \"\nExit code: $?\"";

    var output = $("#output");
    output.text('');
    var to_compile = {
        "src": code.getValue(),
        "cmd": cmd,
    };

    output.text("Executing... Please wait.");

    $.ajax({
        url: "http://coliru.stacked-crooked.com/compile",
        type: "POST",
        data: JSON.stringify(to_compile),
        contentType:"text/plain; charset=utf-8",
        dataType: "text"
    }).done(function(data) {
        output.text(data);
    }).fail(function(data) {
        output.text("Server error: ", data);
    });
};