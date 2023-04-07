/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('dvhfiles', {
    id: {
      autoIncrement: true,
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true
    },
    id4: {
      type: DataTypes.STRING(10),
      allowNull: true
    },
    id7: {
      type: DataTypes.STRING(10),
      allowNull: true
    },
    filename: {
      type: DataTypes.STRING(500),
      allowNull: true
    },
    isdifferential: {
      type: DataTypes.STRING(10),
      allowNull: true,
      comment: '1: is differential , 0: not differential'
    }
  }, {
    sequelize,
    tableName: 'dvhfiles'
  });
};
