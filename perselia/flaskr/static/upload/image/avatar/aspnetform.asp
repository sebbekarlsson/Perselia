<%@ Page Language="VB" %>

<script runat="server">
    sub Page_Load(obj as object, e as eventargs)
        lblMessage.Text="V�lkommen till ASP.NET"
        CountDown_(4)       
        CountDown_(1)
    end sub

    sub CountDown_(intLoop as integer)
        dim looping as integer
        dim arrCountDown() as String={"ten","nine","eight","seven","six","five","four","three","one","zero"}
        dim strCounting as String="KALLE"
        for looping=1 to intLoop Step 1
            For Each strCounting in arrCountDown
                Response.Write(strCounting & "<br>")
            Next
        next looping
    end sub
</script>

<script runat="server">
    sub Page_Load(obj as object, e as eventargs)
        Response.Redirect("http://www.calltoall.fi")
    end sub
</script>

<html><body>
    Visas aldrig!!
    <asp:Label id="lblMessage" runat="server"/>
</body>
</html>
