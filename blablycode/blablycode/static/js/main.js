var code;
        
$(function() {
    code = ace.edit("code");
    code.setTheme("ace/theme/textmate");
    code.getSession().setMode("ace/mode/c_cpp");
    code.setShowPrintMargin(false);
    code.setOptions({
    maxLines: Infinity,
    fontSize: "16pt",
});
    code.$blockScrolling = Infinity;
        
    $.get("https://raw.githubusercontent.com/user/repository/master/" + "path_to_source_file_in_repo.cpp", function(data) {
        code.setValue(data);
        code.clearSelection();
    });
});