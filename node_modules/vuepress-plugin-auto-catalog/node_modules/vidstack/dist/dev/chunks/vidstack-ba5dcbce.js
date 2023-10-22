const SET_AUTO = Symbol("SET_AUTO_QUALITY" ), ENABLE_AUTO = Symbol("ENABLE_AUTO_QUALITY" );
const QualitySymbol = {
  _setAuto: SET_AUTO,
  _enableAuto: ENABLE_AUTO
};

function coerceToError(error) {
  return error instanceof Error ? error : Error(JSON.stringify(error));
}

export { QualitySymbol as Q, coerceToError as c };
