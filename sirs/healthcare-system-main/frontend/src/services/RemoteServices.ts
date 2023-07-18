
import axios from 'axios';
import LoginDto from "../models/LoginDto";
import SAHError from "../models/SAHError";
import SignUpDto from "@/models/SignUpDto";

const httpClient = axios.create();
httpClient.defaults.timeout = 50000;
httpClient.defaults.baseURL = process.env.VUE_APP_ROOT_API;
httpClient.defaults.headers.post['Content-Type'] = 'application/json';

export default class RemoteServices {
    static async login(loginDto: LoginDto): Promise<string> {
        /* TODO Mudar Local Host*/
        return httpClient
            .post('https://localhost:8443/login', loginDto)
            .then((response) => response.data)
            .catch(async (error) => {
                throw new SAHError(
                    await this.errorMessage(error),
                    error.response.data.code
                );
            });
    }

    static async signup(signUpDto: SignUpDto): Promise<string> {
        /* TODO Mudar Local Host*/
        return httpClient
            .post('https://localhost:8443/signup', signUpDto)
            .then((response) => response.data)
            .catch(async (error) => {
                throw new SAHError(
                    await this.errorMessage(error),
                    error.response.data.code
                );
            });
    }

    static async errorMessage(error: any): Promise<string> {
        if (error.message === 'Network Error') {
            return 'Unable to connect to server';
        } else if (error.message.split(' ')[0] === 'timeout') {
            return 'Request timeout - Server took too long to respond';
        } else if (error.response?.data?.message) {
            return error.response.data.message;
        } else {
            return 'Unknown Error - Contact admin';
        }
    }
}