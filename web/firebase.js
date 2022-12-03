// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCCf3w3BIMwULNLeno26zDqbbFfRbrMM-I",
  authDomain: "controlrobot-8132b.firebaseapp.com",
  projectId: "controlrobot-8132b",
  storageBucket: "controlrobot-8132b.appspot.com",
  messagingSenderId: "323520006093",
  appId: "1:323520006093:web:9565c1e5dfe7dbc2dd6684",
  measurementId: "G-R0CK43FMJS"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);