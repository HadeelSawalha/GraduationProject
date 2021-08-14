import jquery from 'jquery';

global.$ = jquery;
global.jQuery = jquery;
import './semanticui'

import 'datatables.net';
import 'datatables.net-dt/css/jquery.dataTables.css';


    $(document).ready( function () {
    $('#myTable').DataTable();
} );
