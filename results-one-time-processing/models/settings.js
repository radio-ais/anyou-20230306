/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('settings', {
    id: {
      autoIncrement: true,
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true
    },
    createdat: {
      type: DataTypes.DATE,
      allowNull: true,
      defaultValue: sequelize.fn('current_timestamp')
    },
    updatedat: {
      type: DataTypes.DATE,
      allowNull: true
    },
    key_: {
      type: DataTypes.STRING(100),
      allowNull: true,
      unique: true
    },
    value_: {
      type: DataTypes.STRING(100),
      allowNull: true
    },
    values_: {
      type: DataTypes.STRING(100),
      allowNull: true
    },
    jvalues_: {
      type: DataTypes.STRING(500),
      allowNull: true
    }
  }, {
    sequelize,
    tableName: 'settings'
  });
};
