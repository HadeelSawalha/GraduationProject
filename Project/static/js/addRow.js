var count=1;
$("#btnaddpatient").click(function(){

  $("#container").append(addNewRow(count));
  count++;
});

function addNewRow(count){
      var newrow=  '<tr>'+
                            '<td>1</td>'+
                            '<td>Dakota Rice</td>'+
                            '<td>'+
                              ' <button type="submit" class="btn btn-info btn-fill pull-center">Upload</button>'+
                         '   </td>'+
                         '   <td>'+
                               ' <a class="Symptoms" id="myFile" title="View" data-toggle="tooltip"><i'+
                                        'class="pe-7s-look"></i></a>'+
                                '<div id="myModelFile" class="File">'+
                                    '<span class="close">&times;</span>'+
                                    '<div class="modal-content-File">'+
                                        '<div id="text" class="col-md-6">'+
                                            '<label class="lable">Information</label><br>'+
                                            '<textarea class="info" style="width: 120%;height: 150px;"'+
                                            '          readonly>jbjbjbj</textarea><br><br>'+
                                           ' <label class="lable">Symptoms</label><br>'+
                                          '  <textarea class="info" readonly'+
                                         '             style="height: 90px; width: 120%;">jvjbj</textarea><br><br>'+
                                         '   <label class="lable">Medical Examinations</label><br>'+
                                            '<textarea class="info" readonly'+
                                                  '    style="width: 120%;height: 150px;">fdbbbbbbbbb</textarea><br><br>'+
                                           ' <label class="lable">Result</label><br>'+
                                            '<textarea class="info" readonly'+
                                                    '  style="height: 50px;width: 120%">tedhdhd</textarea><br><br>'+
                                            '<label class="lable">Type</label><br>'+
                                            '<textarea class="info" readonly'+
                                              '        style="height: 50px;width: 120%">tedhdhd</textarea><br><br>'+
                                           ' <label class="lable">Score</label><br>'+
                                           ' <textarea class="info" readonly'+
                                                     ' style="height: 50px;width: 120%">tedhdhd</textarea><br><br>'+
                                          '  <label class="lable">Treatment</label>'+

                                          '  <textarea class="info" readonly'+
                                         '             style="height: 90px;width: 120%">ngngfbcf</textarea><br><br>'+
                                       ' </div>'+
                                       ' <div class="col-md-6">'+
                                         '   <img id="img01" src="/static/img/homepatient1.jpg">'+
                                     '   </div>'+


                                  '  </div>'+
                                '</div>'+
                           ' </td>'+

                           ' <td>'+

                              '  <a class="edit" title="Edit"><i class="pe-7s-pen"></i></a>'+
                              '  <a class="delete" title="Delete"><i'+
                                      '  class="pe-7s-trash"></i></a>'+
                          '  </td>'+
                      '  </tr>';
  return newrow;
}

