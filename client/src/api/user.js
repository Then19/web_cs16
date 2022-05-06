import axios from "axios";
import config from "./config.json";


export function getUsersList(limit = 25, skip = 0) {
    return axios.get(config.hostname + `users/top?limit=${limit}&skip=${skip}`)
        .then(resp => {
            return resp.data
        }).catch(err => {
            return {}
        })
}

export function getUsersTop() {
    return axios.get(config.hostname + `users/top_info`)
        .then(resp => {
            return resp.data
        }).catch(err => {
            return {}
        })
}
