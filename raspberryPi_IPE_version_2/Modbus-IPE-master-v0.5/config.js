export const slaveConfig = {
    port: "/dev/ttyXRUSB0",
    baudRate: 115200,
    parity: "none",
    dataBits: 8,
    stopBits: 1
};

export const cseUrl = 'http://127.0.0.1:3000';

export const cntUrls = {
    battery: '/TinyIoT/battery',
    energyGeneration: '/TinyIoT/energyGeneration',
    energyConsumption: '/TinyIoT/energyConsumption'
}

export const subRn = {
    battery : ["cnd", "rn", "level", "current", "voltage", "power", "maxvolt", "minvolt", "temp", "charging", "discharging"],
    energyGeneration : ["cnd", "rn", "power", "current", "voltage", "daily", "monthly", "annual", "total", "maxvolt", "minvolt"],
    energyConsumption : ["cnd", "rn", "power", "current", "voltage", "daily", "monthly", "annual", "total"]
}

//export const cntUrls = {
//    battery: '/~/in-cse/fcnt-285278795',
//    energyGeneration: '/~/in-cse/fcnt-477048984',
//    energyConsumption: '/~/in-cse/fcnt-800816461'
//};
