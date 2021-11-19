function _0x456254()
/*Scope Closed:false | writes:true*/ {
    for (var _0x5da681 = Math.round(new Date().getTime() / 1000).toString(), _0x2a83dd = arguments.length, _0x31a891 = new Array(_0x2a83dd), _0x596a02 = 0; _0x596a02 < _0x2a83dd; _0x596a02++)
        _0x31a891[_0x596a02] = arguments[_0x596a02];

    _0x31a891.push(_0x5da681);
    var _0xf7c3c7 = _0x189cbb.SHA1(_0x31a891.join(',')).toString(_0x189cbb.enc.Hex)
    var _0x3c8435 = [_0xf7c3c7, _0x5da681].join(',')
    return _0x358b1f.encode(_0x3c8435);
}