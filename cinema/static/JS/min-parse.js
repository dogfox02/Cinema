(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){
(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){
var script = document.querySelector('[magnet]')
magnet = script.getAttribute('magnet')
torrentId = magnet
torrentId = torrentId.replace(/\&amp;/g,'&');

console.log(torrentId)

const client = new WebTorrent()
client.add(torrentId, function (torrent) {
console.log("Here")
// Torrents can contain many files. Let's use the .mp4 file
const file = torrent.files.find(function (file) {
       return file.name.endsWith('.mp4')
})

// Display the file by adding it to the DOM.
// Supports video, audio, image files, and more!
file.appendTo('.myVideo')
})
},{}]},{},[1]);

},{}]},{},[1]);
