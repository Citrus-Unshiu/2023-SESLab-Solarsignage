export const slaveConfig = {
    port: "/dev/ttyXRUSB0",
    baudRate: 115200,
    parity: "none",
    dataBits: 8,
    stopBits: 1
};

export const cseUrl = 'http://127.0.0.1:3000';

export const cntUrls = {
    battery: '/TinyIoT',
    energyGeneration: '/TinyIoT',
    energyConsumption: '/TinyIoT'
}

//export const cntUrls = {
//    battery: '/~/in-cse/fcnt-285278795',
//    energyGeneration: '/~/in-cse/fcnt-477048984',
//    energyConsumption: '/~/in-cse/fcnt-800816461'
//};
