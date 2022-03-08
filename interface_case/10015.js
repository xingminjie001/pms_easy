//AES-CBC模式加解密
var CryptoJS = require("crypto-js");
var AesKey = "cloudwisdomadjsn";
var CBCIV = "5721678222017913";
//加密选项
var CBCOptions = {
    iv: CryptoJS.enc.Utf8.parse(CBCIV),
    mode:CryptoJS.mode.CBC,
    padding: CryptoJS.pad.Pkcs7
}
//AES加密
function encrypt(data){
    var key = CryptoJS.enc.Utf8.parse(AesKey);
    var secretData = CryptoJS.enc.Utf8.parse(data);
    var encrypted = CryptoJS.AES.encrypt(
        secretData,
        key,
        CBCOptions
    );
    return encrypted.toString();
}
//AES解密
function decrypt(data){
    var key = CryptoJS.enc.Utf8.parse(AesKey);
    var decrypt = CryptoJS.AES.decrypt(
        data,
        key,
        CBCOptions
    );
    return CryptoJS.enc.Utf8.stringify(decrypt).toString();
}

//HmacSHA1签名
//let CryptoJS = hitchhiker.require("crypto-js");
let Lc_Sid = '9fac9a36c2a845c0209ff4dc3dd25c75';
let SecretKey = 'ee12ba05cd22f998621b2bbae3f3bbba';
//let Lc_Ts = '1587711799182';
//let Lc_Ts = new Date().getTime();
let Lc_Ts = '1547436455979';
function Sign(req_body) {
    var obj={
        Lc_Sid:Lc_Sid,
        SecretKey:SecretKey,
        Lc_Ts:Lc_Ts,
        //Lc_Ts:'1587711799182',
        // QueryStringValue:'http://rezenhotels.com?a=test&b=testb',
        body:req_body,
    }
    function createString(obj={}){
        var arr=[];
        for (key in obj){
            arr.push(obj[key])
        }
        arr.sort();
        var str=arr.join('');
        return str
    }
    var signing = createString(obj)
    var hash = CryptoJS.HmacSHA1(signing,SecretKey)
    console.log('获取签名需要的串：')
    console.log(signing)
    var sign = hash.toString(CryptoJS.enc.Base64);
    console.log('获取签名：')
    console.log(sign)
    console.log('获取当前时间戳：')
    console.log(Lc_Ts)
    //return [sign,Lc_Ts]
    return { sign:sign,lc_ts:Lc_Ts}
}


//encodeUtf8
function encodeUtf8(text) {
    const code = encodeURIComponent(text);
    const bytes = [];
    for (var i = 0; i < code.length; i++) {
        const c = code.charAt(i);
        if (c === '%') {
            const hex = code.charAt(i + 1) + code.charAt(i + 2);
            const hexVal = parseInt(hex, 16);
            bytes.push(hexVal);
            i += 2;
        } else bytes.push(c.charCodeAt(0));
    }
    return bytes;
}

//decodeUtf8
function decodeUtf8(bytes) {
    var encoded = "";
    for (var i = 0; i < bytes.length; i++) {
        encoded += '%' + bytes[i].toString(16);
    }
    return decodeURIComponent(encoded);
}
//date
function getDate(){
    var newDate = new Date();
    var year = newDate.getFullYear();
    var month = newDate.getMonth() + 1;
    month = month > 9 ? month : "0" + month;
    var day = newDate.getDate();
    day = day > 9 ? day : "0" + day;
    var today = year + '-' + month + "-" + day;
    var tomorrow = year + '-' + month + "-" + (day+2);
    console.log("当前日期：")
    console.log(today)
    console.log(tomorrow)
    return today,tomorrow
}

// const request_data1 = '{"RQModel_RtInfo":[{"acctNum":"2501764","name":"xmj","rmNum":"1128","arrDate":"2020-03-18","dptDate":"2020-03-19","crtfType":"警官证","crtfNum":"111","sex":"男","geo1":"中国","geo2":"北京","birthday":"2001-03-12","nation":"汉","address":"海淀区"}],"grpcd":"lc","htlcd":"lc01","staffcd":"9897","token":"69C510BFC59E8F300FE11F968D0DF937F4A88BFF","staffpassword":"sunwood","isformal":"True","mac":"6C-0B-84-08-06-78"}'
//
// const request_data = request_data1.replace(/^\s*|\s*$/g,"");
// console.log('更新请求数据：')
// console.log(request_data)
//
// const request_data_encrypt = encrypt(request_data)
// console.log('请求数据加密：')
// console.log(request_data_encrypt)
//
// const request_data_crypt = decrypt(request_data_encrypt)
// console.log('请求数据再解密：')
// console.log(request_data_crypt)
//


request_data = '{"RQData_ResvInfo":[{"acctNm":"邢敏杰","rmNum":"9982","ArrDate":"2021-11-17","DptDate":"2021-11-17","rtCd":"0BAR01","crdtNum":"","rmTaxCd":"ROOM","GstArrTm":"17:15:23","GstDptTm":"17:15:23","GrpNum":"","TaNum":"","OrgCd":"","notice":"备注","Telephone":""}],"grpcd":"lc","htlcd":"100015","staffcd":"xingminjie","token":"A37B083AC60359D6E868C356AADE449A879CD873","staffpassword":"lc123456","isformal":"True","mac":"D4-3D-7E-C6-91-8B"}'
console.log(typeof(request_data))

//房号
var roomnum = (JSON.parse(request_data)).RQData_ResvInfo[0].rmNum
console.log(roomnum)
// hitchhiker.setEnvVariable('roomnum',roomnum);
//姓名
var acctnm = (JSON.parse(request_data)).RQData_ResvInfo[0].acctNm
console.log(acctnm)
// hitchhiker.setEnvVariable('acctnm',acctnm);

var items = ['邢敏杰','石美','吕建强','李冬','王战磊','王磊','张瑜','刘建设','李延铮'];
var acctname = items[Math.floor(Math.random()*items.length)];
//hitchhiker.setEnvVariable('acctname',acctname);
console.log(acctname)

request_tranAmt = '{"RQData_PostTran":[{"acctNum":"111","tranCd":"101","tranAmt":"298","trnRef":""}]}'

//房号
var tranAmt = (JSON.parse(request_tranAmt)).RQData_PostTran[0].tranAmt
console.log(tranAmt)
// hitchhiker.setEnvVariable('tranAmt',tranAmt);















