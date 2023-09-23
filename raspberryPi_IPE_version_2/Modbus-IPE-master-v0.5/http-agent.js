import request from 'request-promise';
import {cseUrl, cntUrls, subRn}  from './config'
//import slave from './app.js'

export async function uploadMonitoringData(data) {
    for (const module in cntUrls) {
        /*if(JSON.stringify(data[module]) === '{}'){
            console.log('NULL data')
	    slave.close()
	    slave = await connect()
	    console.log('reconnected the slave 2')
	}*/
	try{
		await updateContainer(cseUrl.concat(cntUrls[module]), data[module])
	} catch(e){
		console.log("updateContainer error")
	}
    }
    // await updateFlexContainer(cseUrl.concat(fcntUrls['battery']), data['battery'])
}

async function updateFlexContainer(url, data) {
    let options = {
        method: 'PUT',
        uri: url,
        port: 3000,
        body: {
            "m2m:fcnt": data
        },
        headers: {
            'Accept': 'application/json',
            'X-M2M-RI': 'ipe',
            'X-M2M-Origin': 'admin:admin',
            'Content-Type': 'application/json;ty=28'
        },
        json: true
    };
    try {
	console.log(data);
        return await request(options);
    } catch (e) {
        console.log('PUT request error: ', e);
    }
}

async function updateContainer(url, data) {
    //data 가공해서 하나하나 넣어야됨
    for (const item of subRn) {
        let options = {
            method: 'PUT',
            uri: url + "/" + item,
            port: 3000,
            body: {
                "m2m:cin": data
            },
            headers: {
                'Accept': 'application/json',
                'X-M2M-RI': 'ipe',
                'X-M2M-Origin': 'admin:admin',
                'Content-Type': 'application/json;ty=4'
            },
            json: true
        };
        try {
        console.log(data);
            return await request(options);
        } catch (e) {
            console.log('PUT request error: ', e);
        }
    }
}

async function reconnect(url, data){
	let options = {
        uri: url,
        method: 'POST',
        body:{

        },
        json:true //json으로 보낼경우 true로 해주어야 header값이 json으로 설정됩니다.
    };
    try{
        return await request(options);
    } catch (e) {
	console.log(e);
        console.log('Reconnect ERROR');
    }
}
