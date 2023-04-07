/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('features', {
    id: {
      autoIncrement: true,
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true
    },
    id4: {
      type: DataTypes.STRING(10),
      allowNull: true,
      comment: '4 digit id'
    },
    id7: {
      type: DataTypes.STRING(10),
      allowNull: true,
      comment: '7 digit id'
    },
    rtdose: {
      type: DataTypes.STRING(10),
      allowNull: true
    },
    rp: {
      type: DataTypes.STRING(10),
      allowNull: true,
      comment: 'rp positive:1 , negative:0'
    },
    ecog: {
      type: DataTypes.STRING(10),
      allowNull: true
    },
    copd: {
      type: DataTypes.STRING(10),
      allowNull: true
    },
    ild: {
      type: DataTypes.STRING(10),
      allowNull: true
    },
    fev1: {
      type: DataTypes.STRING(10),
      allowNull: true
    },
    fev1fvc: {
      type: DataTypes.STRING(10),
      allowNull: true
    },
    dlco: {
      type: DataTypes.STRING(10),
      allowNull: true
    },
    age: {
      type: DataTypes.STRING(10),
      allowNull: true
    },
    dob: {
      type: DataTypes.STRING(10),
      allowNull: true
    },
    gender: {
      type: DataTypes.STRING(10),
      allowNull: true
    },
    pathg: {
      type: DataTypes.STRING(10),
      allowNull: true
    },
    t: {
      type: DataTypes.STRING(10),
      allowNull: true
    },
    n: {
      type: DataTypes.STRING(10),
      allowNull: true
    },
    institution: {
      type: DataTypes.STRING(10),
      allowNull: true
    },
    exclude: {
      type: DataTypes.STRING(10),
      allowNull: true,
      comment: '1: exclude, 0: not exclude'
    },
    excludereason: {
      type: DataTypes.TEXT,
      allowNull: true
    },
    LV05: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    LV10: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    LV20: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    LV30: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    LV40: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    LV50: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    filenamedvh: {
      type: DataTypes.TEXT,
      allowNull: true
    },
    volumelung: {
      type: DataTypes.STRING(10),
      allowNull: true
    },
    meandose: {
      type: DataTypes.STRING(10),
      allowNull: true
    },
    PTV: {
      type: DataTypes.STRING(10),
      allowNull: true
    },
    filenamebase: {
      type: DataTypes.STRING(100),
      allowNull: true
    },
    LV05f: {
      type: DataTypes.FLOAT,
      allowNull: true
    },
    LV10f: {
      type: DataTypes.FLOAT,
      allowNull: true
    },
    LV20f: {
      type: DataTypes.FLOAT,
      allowNull: true
    },
    LV30f: {
      type: DataTypes.FLOAT,
      allowNull: true
    },
    LV40f: {
      type: DataTypes.FLOAT,
      allowNull: true
    },
    LV50f: {
      type: DataTypes.FLOAT,
      allowNull: true
    }
  }, {
    sequelize,
    tableName: 'features'
  });
};
