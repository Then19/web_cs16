import axios from "axios";
import config from "./config.json";


export function getServersInfo() {
    return axios.get(config.hostname + 'server/server_list')
        .then(resp => {
            return resp.data
        }).catch(err => {
            return []
        })
}
