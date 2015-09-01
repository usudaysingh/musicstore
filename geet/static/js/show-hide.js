<script type="text/javascript">
        /* If wanted to run when page is loaded. */
        $(function() {
            // Handler for .ready() called. 
            visibility("detail");
        });

        function visibility(reportType) {
            if(reportType == "detail") {
                $('#executive_summary').show();
            }
            else {
                $('#executive_summary').hide();
            }
        }
    </script>
